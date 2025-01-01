import { Alert, AlertDescription, AlertTitle } from "@shadcn/ui";

export default function AlertComponent({ children, type, title }) {
  return (
    <Alert type={type}>
      {title && <AlertTitle>{title}</AlertTitle>}
      <AlertDescription>{children}</AlertDescription>
    </Alert>
  );
}
